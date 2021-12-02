interface A
{
	
	interface B
	{
		void msg();
	}
}
abstract class Hello
{
	Hello()
	{
		System.out.println("i am amala");
	}
	abstract void hi();
	void hey()
	{
		System.out.println("i m fine");
	}
}
class Bye extends Hello
{
	void hi()
	{
		System.out.println("nice meeting u");
	}
}
public class Manner implements A.B

{
public void msg()
	{
		System.out.println("Hello");
	}
	public static void main(String args[])
	{
		Hello obj=new Bye();
		obj.hi();
		obj.hey();
		A.B obj1=new Manner();
		obj1.msg();
		
	}
}