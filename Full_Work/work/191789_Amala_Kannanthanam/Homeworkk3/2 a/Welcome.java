interface Friends
{
	void happy();
}
interface Family extends Friends
{
	void life();
}
class Welcome implements Family
{
	public void happy()
	{
		System.out.println("Life is strange");
	}
	public void life()
	{
		System.out.println("Be happy");
	}
	public static void main(String args[])
	{
		Welcome obj =new Welcome();
		obj.happy();
		obj.life();
	}
}