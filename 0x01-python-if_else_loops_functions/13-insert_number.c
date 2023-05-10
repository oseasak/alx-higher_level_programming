#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: Number to insert.
 * Author - Asak Erhumuose
 * Return: If function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *ned;

	ned = malloc(sizeof(listint_t));
	if (ned == NULL)
		return (NULL);
	ned->n = number;

	if (node == NULL || node->n >= number)
	{
		ned->next = node;
		*head = ned;
		return (ned);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	ned->next = node->next;
	node->next = ned;

	return (ned);
}
