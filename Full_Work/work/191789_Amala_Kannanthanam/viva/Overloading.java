class Adder{  

static int add(int a, int b)
{
	return a+b;
}  
static double add(double a, double b)
{
	return a+b;
}  
}  
public class Overloading{  
void la()
	{
		for(int i=0;i<5;i++)
		{
			
			System.out.println(i);
		}

	}
public static void main(String[] args){  
	String s="ADDITION";
	System.out.println("Name:"+s);
	System.out.println("Sum:" +Adder.add(10,10));  
	System.out.println("Sum:" +Adder.add(11.3,11.6));  
	Overloading obj = new Overloading();
	obj.la();
}}  