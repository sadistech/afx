#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/types.h>
#include<signal.h>

#define PID_MAX_FILE_LEN 12

int main(int argc, char **argv) {
	FILE *ifile = NULL;

	char *pid_path = argv[1];

	printf("reading pid file: %s\n", pid_path);

	if (!(ifile = fopen(pid_path, "r")))
		exit(EXIT_FAILURE);

	char str_pid[PID_MAX_FILE_LEN + 1] = "";

	fread(str_pid, PID_MAX_FILE_LEN, 1, ifile);

	int pid = atoi(str_pid);

	if (!(pid > 1)) {
		printf("pid <= 1!!!! ack!\n");
		exit(EXIT_FAILURE);
	}

	kill(pid, SIGTERM);

	exit(EXIT_SUCCESS);
}
