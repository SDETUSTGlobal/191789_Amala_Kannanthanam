class School{  

  void teach()
  {
	  System.out.println("Taking class");
  }  
}  
class Teacher extends School{  
  void teach()
  {
	  System.out.println("class is till 8");
	 }  
  
  public static void main(String args[])
  {  
    School b = new Teacher();
    b.teach(); 
	Teacher c =new Teacher();
	System.out.println(c instanceof School);
  }  
}  