#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int infinite_while(void);

/**
 * main - create 5 zombie processes
 *
 * Return: exit status 0
 */
int main(void)
{
	pid_t zombie_pid;
	int i = 0;

	for (; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", zombie_pid);
	}

	infinite_while();

	return (0);
}

/**
 * infinite_while - infinite loop
 *	sleep after creating zombie child process
 *
 * Return: exit 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}

	return (0);
}
