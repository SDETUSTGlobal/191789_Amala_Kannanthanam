class Birds
{
	protected void fly()
	{
		System.out.println("Crow");
	}
	
	public void sit()
	{
		System.out.println("Sparrow");
		
	}
	void walk()
	{
		System.out.println("Penguins");
	}
	
}
public class Animals extends Birds
{
	public static void main(String args[])
	{
		Animals obj = new Animals();
		obj.fly();
		obj.sit();
	obj.walk();
	Animals obj1 =new Animals();
		obj1.eat();}
	private void eat()
	{
		System.out.println("Vulgers");
	}
		
	
}