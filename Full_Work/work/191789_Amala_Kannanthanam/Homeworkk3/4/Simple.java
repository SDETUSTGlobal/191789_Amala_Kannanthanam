package pack; 
interface print1
{
	void print();
}
 class Ann{
	 public void a()
	 {
		 System.out.println("Bye");
	 }
	 
 }
public class Simple implements print1
{  
public void print()
{
	System.out.println("hello");
}
public void write()
{
	System.out.println("hw r u??");
}
 public static void main(String args[])
 {  

	Simple obj =new Simple();
	Ann obj1=new Ann();
	obj1.a();
	
	obj.print();
	obj.write();
   }  
}
