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
pid_t pid;
int i = 0;

while (i < 5)
{
	pid = fork();
	if (pid > 0)
	{
	printf("Zombie process created, PID: %d\n", pid);
	i++;
	}
	else
		exit(0);
}
infinite_while();

return (0);
}
