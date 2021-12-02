interface Rain
{
	void umbrella();
}
interface Rainning
{
	void raincoat();
}
class Weather implements Rain,Rainning
{
	public void umbrella()
	{
		System.out.println("It is rainning");
	}
	public void raincoat()
	{
		System.out.println("It is beautiful");
	}
	
	public static void main(String args[])
	{
		Weather obj = new Weather();
		obj.umbrella();
		obj.raincoat();
	}
}