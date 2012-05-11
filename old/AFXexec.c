/*
**	AFXexec.c
**
**	7/11/05
**	spike grobstein
**	spike@sadistech.com
**
**	executed from AFX to launch a module
**
**	usage: afxexec <pid_file> <exec_path> <args> ...
*/

#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

#define PID_ERROR 1
#define PID_SUCCESS 0

void check_pid_file(char *path);
int write_pid_file(char *path);

int main(int argc, char **argv) {	
	*argv++; //shift argv[0] off the front (THIS executable)
	char *pid_path = *argv++;

	check_pid_file(pid_path); //delete the pid file before writing...
	
	if (write_pid_file(pid_path) == PID_ERROR)
		exit(EXIT_FAILURE);
	
	char *exec_path = *argv;
	
	int ret_code = execv(exec_path, argv);

	//if we get to this point in the program, something went wrong!
	
	printf("AN ERROR OCCURRED!!!! ACK!\n");
	
	check_pid_file(pid_path); //clean up...
	
	exit(EXIT_FAILURE);
}

int write_pid_file(char *path) {
	/*
	**	writes the current process's PID to a file,
	**	since the process we're gonna exec inherits our PID
	**	returns PID_ERROR on failure
	**	returns PID_SUCCESS on success (duh)
	*/
	
	FILE *ofile;

	if (!(ofile = fopen(path, "w"))) {
		return PID_ERROR;
	}

	int pid = getpid();

	char str_pid[12] = "";

	sprintf(str_pid, "%d", pid);

	fputs(str_pid, ofile);

	fclose(ofile);

	return PID_SUCCESS;
}

void check_pid_file(char *path) {
	/*
	**	checks to see if the PID file exists
	**	deletes it, if it does.
	**
	**	gets run before setting the PID and if exec fails
	*/

	unlink(path);
}
