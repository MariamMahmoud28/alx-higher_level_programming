#include "lists.h"

/**
 * aux_palind - Recursive function to check if a linked list is a palindrome.
 * @left: Pointer to the left end of the sublist.
 * @right: Pointer to the right end of the sublist.
 * Return: 1 if the sublist is a palindrome, 0 otherwise.
 */
int aux_palind(listint_t **left, listint_t *right) {
    int is_palindrome;

    if (right == NULL)
        return 1;

    is_palindrome = aux_palind(left, right->next);
    if (!is_palindrome)
        return 0;

    is_palindrome = (right->n == (*left)->n);
    *left = (*left)->next;

    return is_palindrome;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    return aux_palind(head, *head);
}
