class Person
{ 
final int a=10; 
void ann()
	{
		 
	System.out.println("loves to talk");
	System.out.println(a);
	
	}  
}  
class Doctor extends Person
{  
void treat()
{
	System.out.println("helps people");}  
}  
final class Engineer extends Person
{  

final void create()
	{
	System.out.println("make a better place");
	}  
}  
class TestInheritance3
{  
public static void main(String args[]){  
Engineer c=new Engineer();  
c.create();  
c.ann();  

}}  