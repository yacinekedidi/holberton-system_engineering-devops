#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

/**
 * infinite_while - sleep for eternity
 * @void : nothing
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - sleep for eternity
 * @void : nothing
 * Return: Always 0.
 */
int main(void)
{
pid_t pid, i = 0, status;

while (i < 5)
{
	pid = fork();
	if (pid < 0)
	{
		perror("some wrong");
		exit(1);
	}
	if (pid == 0)
		exit(0);
	printf("Zombie process created, PID: %d\n", pid);
	i++;
}
infinite_while();

return (0);
}
