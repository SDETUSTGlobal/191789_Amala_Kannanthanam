class Butterfly
{
	String motion="eat";
	Butterfly()
	{
		System.out.println("go away");
	}
}

class Pupa extends Butterfly
{
	
	String motion="move";
	void stage()
	{
		System.out.println("fly");
		motion();
	}
	void motion()
	{
		System.out.println(motion);
		System.out.println(super.motion);
	}
	Pupa()
	{
		super();
	}
}

class Caterpiller extends Pupa
{
	void stage()
	{
		System.out.println("bye");
		super.stage();
	}
	
}

class Mul
{
	public static void main(String args[])
	{
		Caterpiller ob=new Caterpiller();
		ob.stage();
	}
}