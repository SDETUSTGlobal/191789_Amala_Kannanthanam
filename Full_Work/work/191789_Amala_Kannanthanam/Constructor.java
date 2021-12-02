class Constructor
{
	int a,b,c;

	String name;
	
	Constructor()
	{
		
	}
	Constructor(int i)
	{
		a=i;
	}
	Constructor(int i,String n)
	{
		
		
		a=i;
		name=n;
	}
	Constructor(int i,int j,int k,String n)
	{
		a=i;
		b=j;
		c=k;
		name=n;
	}
	void addition()
	{
		System.out.println(a+b+c);
		System.out.println(name);
	}
	void subtraction()
	{
		System.out.println((a-b)-c);
		System.out.println(name);
	}
	void multiplication()
	{
		System.out.println(a*b*c);
		System.out.println(name);
	}
	void division()
	{
		System.out.println((a/b)/c);
		System.out.println(name);
	}
	public static void main(String args[])
	{
		
		Constructor ob1=new Constructor();
		Constructor ob2=new Constructor(20);
		Constructor ob3=new Constructor(20,"AMALA");
		Constructor ob4=new Constructor(20,10,5,"AMALA");
		
		
		ob1.a=20;
		ob1.b=10;
		ob1.c=5;
		ob1.name="AMALA";
		
		
		ob2.b=10;
		ob2.c=5;
		ob2.name="AMALA";
		
		
		ob3.b=10;
		ob3.c=5;
		
		
	
		System.out.println("Addition using default construction overloading");
		ob1.addition();
		System.out.println("Subtraction using one parameter construction overloading");
		ob2.subtraction();
		System.out.println("Multiplication using two parameter construction overloading");
		ob3.multiplication();
		System.out.println("Division using four parameter construction overloading");
		ob4.division();
		}
}
