abstract class Cat
{
	abstract void mweo();  
}  
class Persian extends Cat
{  
	void mweo()
	{
		System.out.println("wants food");
	}  
	public static void main(String args[])
	{  
		Cat obj = new Persian();  
		obj.mweo();  
	}  
}  