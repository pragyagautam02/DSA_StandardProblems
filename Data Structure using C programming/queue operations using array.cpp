#include<stdio.h>
#include<stdlib.h>
#define MAX 5
int queue_array[MAX];
int rear = -1;
int front = -1;
void main()
{
   int choice;
   while(1)
   {
     printf("1.Insert element to queue\n");
     printf("2.Delete element from queue\n");
     printf("3.Display all elements of queue\n");
     printf("4.Quite\n");
     printf("Enter ur choice: ");
     scanf("%d", &choice);
     switch(choice)
     {
        case 1:
        insert();
        break;
        case 2:
        del();
        break;
        case 3:
        display();
        break;
        case 4:
        exit(1);
        default:
        printf("Wrong choice!!\n");
     }
   }
}
