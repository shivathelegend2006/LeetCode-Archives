/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int maxDepth(struct TreeNode* root) {
    if (root==NULL) return 0;
    int l = maxDepth(root->left) + 1;
    int r = maxDepth(root->right) + 1;
    if (l>r) return l;
    else return r;
}