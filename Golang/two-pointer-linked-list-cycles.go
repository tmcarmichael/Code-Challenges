package main

/*
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an
integer pos which represents the position (0-indexed) in
the linked list where tail connects to. If pos is -1, then
there is no cycle in the linked list.
*/

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Determine if given linked list contains cycles
func hasCycle(head *ListNode) bool {
	first, second := head, head
	for first != nil && first.Next != nil {
		first = first.Next.Next
		second = second.Next
		if first == second {
			return true
		}
	}
	return false
}
