/*
**	AFXexec3.c
**
**	7/14/05
**	spike grobstein
**	spike@sadistech.com
**
**	executed from AFX to launch a module
**	forks and does 3 things...
**		a. launches the module (exec path with args)
**		b. loops and waits for certain button press. dies when pressed.
**		c. monitors the processes of a. and b.,
**			if either dies, it kills both and exits cleanly.
**
**	usage: afxexec <exec_path> <args> ...
*/

#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/types.h>
#include<signal.h>
#include<jsw.h>

static int runlevel;
static void MySignalHandler(int s);

static void MySignalHandler(int s) {
	if (s == SIGINT || s == SIGKILL) runlevel = 1;
}

void check_quit_action();

int main(int argc, char **argv) {	
	int pid = 0;
	int my_pid = getpid();

	int exec_pid = 0;
	int js_pid = 0;
	
	printf("%s launched with pid: %d\n", argv[0], my_pid);

	*argv++;
	
	//first, we're gonna fork and launch the program with the child process...
	if ((pid = fork()) < 0) {
		printf("an error occurred whilst forking!!\n");
		exit(EXIT_FAILURE);
	}

	exec_pid = pid;
	
	if (pid == 0) {
		// ok, we're the child process... launch the module...
		
		my_pid = getpid();

		printf("exec'ing with pid: %d\n", my_pid);
		
		char *exec_path = *argv;
		int ret_code = execv(exec_path, argv);

		//if we get this far, something went terribly, terribly wrong...
		
		printf("ACK! An error occurred!!!!!!!!\n");
		exit(EXIT_FAILURE);
	} else {
		if ((pid = fork()) < 0) {
			printf("an error occurred whilst forking to reaper!\n");
			kill(exec_pid, SIGTERM); //kill that exec process
			exit(EXIT_FAILURE);
		}

		js_pid = pid;
		
		if (pid == 0) {
			// loop and check for joystick quit...
			printf("looping... gonna kill %d\n", exec_pid);
			check_quit_action();
			printf("sending kill signal (%d -> %d)\n", my_pid, exec_pid);
			kill(exec_pid, SIGTERM);
			exit(EXIT_SUCCESS);
		} else {
			//be the reaper and check for either process being quit.

			int status = 0;
			waitpid(0, &status, 0);

			printf("oooh, something else died (status: %d). gonna kill %d and %d\n", status, exec_pid, js_pid);

			kill(exec_pid, SIGTERM);
			kill(js_pid, SIGTERM);
		}
			
	}

	printf("ok, complete!");
	
	exit(EXIT_SUCCESS);
}

void check_quit_action() {
	// this is where we loop and check for joystick quit event (buttons 8 and 9);
	
	int i, status;

	const char *device = "/dev/input/js0";
	const char *calib = "/home/spike/.joystick.bak";

	js_data_struct jsd;

	signal(SIGINT, MySignalHandler);

	status = JSInit(&jsd, device, calib, JSFlagNonBlocking);

	if (status != JSSuccess) {
		printf("ERROR with joystick!\n");
		JSClose(&jsd);
		exit(EXIT_FAILURE);
	}

	printf("Initialized joystick: %s\n", jsd.name);

	runlevel = 2;
	while(runlevel >= 2) {
		if (JSUpdate(&jsd) == JSGotEvent &&
				(JSGetButtonState(&jsd, 8) && JSGetButtonState(&jsd, 9))) {
			JSClose(&jsd);
			return;
		}
		usleep(16000);
	}
}
