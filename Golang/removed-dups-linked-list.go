package main

// Given a sorted linked list, delete all duplicates
// such that each element appear only once.
// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head != nil {
		first, second := head, head.Next
		for first != nil && second != nil {
			if first.Val == second.Val {
				second = second.Next
				first.Next = second
			} else {
				second = second.Next
				first = first.Next
			}
		}
	}
	return head
}
