#include "lists.h"
/**
 * insert_node - function to inserts a number into a sorted singly linked list
 * @head: head of the list
 * @number: NUmber to be insert
 * Return: The address of the new node or Null if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	current = *head;
	while (current != NULL && current->n < number)
	{
		current = current->next;
	}
	if (current == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
