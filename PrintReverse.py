
void reversePrint(SinglyLinkedListNode* head) {
    int a[10000];
    int ind=0;
    while(head!=NULL)
    {
        a[ind]=head->data;
        ind++;
        head=head->next;
    }
    for(int j=ind-1;j>=0;j--)
    {
        printf("%d\n",a[j]);
    }

}

