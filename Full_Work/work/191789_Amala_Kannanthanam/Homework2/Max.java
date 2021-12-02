//single inheritance
class Lib
{
String l;
public Lib(String a)
{
l = a;
}
}
public class Max extends Lib {
String l;
public Max(String y1, String y2)
{
super(y1);       
this.l = y2;
System.out.println("Welcome");
}
 
{System.out.println("Hello");
}

public void display()
{
System.out.println(super.l+" and "+l);
}
public static void main(String[] args)
{
Max c = new Max
("Amala","b K");
c.display();
}
}