import java.io.*;
import java.util.Scanner;
public class Switch
{
	public static void main(String args[])
	{
		System.out.println(" 1.Odd Number \n 2.Even Number \n 3.Postive or Negative \n 4.Largest number \n 5.Reverse Digit \n 6.Perfect Square \n Enter the input:");
		Scanner k = new Scanner(System.in);
		int input = k.nextInt();
		//int input=1;
		int l,rev=0;
		switch(input)
		{
			case 1:
				System.out.println("Odd Numbers");
				for(int i=1;i<=100;i++)
				{
					if(i%2!=0)
					{
						System.out.println(i+" ");
					}
				}
				break;
			case 2:
				System.out.println("Even Numbers");
				for(int i=1;i<=100;i++)
				{
					if(i%2==0)
					{
						System.out.println(i+" ");
					}
				}
				break;
			case 3:
				int num;
				System.out.println("Enter a number :");
				Scanner sc = new Scanner(System.in);
				num = sc.nextInt();

				if (num > 0)
				{
					System.out.println("positive integer");
				} 
				else 
				{
				System.out.println("negative integer");
				}
				break;
			case 4:
				int a, b, c, largest, temp;  
 
				Scanner ar = new Scanner(System.in);  

				System.out.println("Enter the first number:");  
				a = ar.nextInt();  
				System.out.println("Enter the second number:");  
				b = ar.nextInt();  
				System.out.println("Enter the third number:");  
				c = ar.nextInt();  
  
				temp=a>b?a:b;  

				largest=c>temp?c:temp;  
				System.out.println("The largest number is: "+largest);  
				break;
			case 5:
				Scanner f =new Scanner(System.in);
				System.out.println("Enter the number to reverse:");
				l = f.nextInt();
				while(l!=0)
				{
					int rem = l%10;
					rev = rev*10+rem;
					l=l/10;
				}
				System.out.println("The reverse number is:" +rev);
				break;
			case 6:
				Scanner ll=new Scanner(System.in);  
				System.out.print("Enter a number: ");   
				int number=ll.nextInt();   
				int sqrt=(int)Math.sqrt(number);
					if(sqrt*sqrt==number)   
    					{
							System.out.println("Yes, the given number is perfect square.");
						}	
						else  
						{
							System.out.print("No, the given number is not perfect square."); 
						}
					  
				break;
			default:
				System.out.println("invalid input");
		}
	}
}