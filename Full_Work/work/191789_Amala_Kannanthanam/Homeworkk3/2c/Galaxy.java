interface Star
{
	
	default void planet()
	{
		System.out.println("default planet");
	}
	
	static int universe(int s)
	{
		return s*s;
	}

}
	class Galaxy implements Star
	{
		public static void main(String args[])
		{
			Galaxy obj=new Galaxy();
			obj.planet();
			System.out.println(Star.universe(3));
			
			
			
		}
	
	}
