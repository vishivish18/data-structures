def binary_search(root, key):
	if root is None or root.value == key:
		return root

	if root.val < key:
		return binary_search(root.right, key)

	return binary_search(root.left, key)

