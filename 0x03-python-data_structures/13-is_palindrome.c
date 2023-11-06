#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/* Define a singly linked list structure */
struct listint_t {
    int n;
    struct listint_t *next;
};

typedef struct listint_t listint_t;

/* Function to reverse a linked list */
listint_t *reverse_list(listint_t *head) {
    listint_t *prev = NULL, *current = head, *next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/* Function to check if a linked list is a palindrome */
int is_palindrome(listint_t **head) {
    if (*head == NULL) {
        return 1; // An empty list is considered a palindrome
    }

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *first_half = *head;
    listint_t *prev = NULL;

    // Use two pointers to find the middle of the list
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    // Split the list into two halves
    prev->next = NULL;

    // Reverse the second half
    listint_t *second_half = reverse_list(slow);

    // Compare the two halves
    while (first_half != NULL && second_half != NULL) {
        if (first_half->n != second_half->n) {
            // Not a palindrome
            return 0;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // If all elements match, it's a palindrome
    return 1;
}
