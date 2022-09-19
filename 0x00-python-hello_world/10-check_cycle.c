#include "list.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checks for cycle
 * @list: poiner to list
 * Retutn: int
 */

int check_cycle(listint_t *list)
{
	listint_int *head;
	head = list;

	while (head != NULL)
	{
		if (head->n == 0)
		{
			return (1);
		}
		else
		{
			return (0);
		}
	}
}
