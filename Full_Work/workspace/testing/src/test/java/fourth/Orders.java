package fourth;
import org.openqa.selenium.By;  
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;  
import cucumber.annotation.en.Given;  
import cucumber.annotation.en.Then;  
import cucumber.annotation.en.When; 
public class Orders {

WebDriver driver= null;
	  @Given("^I am on user order page$")  
	  public void goToWebLogin() {  
	  
	  System.setProperty("webdriver.chrome.driver", "D://eclipse1//Sel_jar//chromedriver_win32//chromedriver.exe");
	  driver= new ChromeDriver();
	  driver.navigate().to("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Process.aspx");  
	  }  
	     
	  @When("^I enter valid data on the page$")  
	  public void enterData(){ 
		  driver.findElement(By.partialLinkText("Order")).click();
			 
		  
		    driver.findElement(By.cssSelector("#ctl00_MainContent_fmwOrder_txtQuantity")).sendKeys("1000");
		    driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtUnitPrice")).sendKeys("80");
			driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]")).click();//xpath
			
			driver.findElement(By.name("ctl00$MainContent$fmwOrder$txtName")).sendKeys("Amala");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox2")).sendKeys("manimala");

			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox3")).sendKeys("kottayam");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox4")).sendKeys("Kerala");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox5")).sendKeys("686543");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_cardList_0")).click();
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox6")).sendKeys("123456789012");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox1")).sendKeys("01/99");
			  
	}
	  @Then("^User login should be successful$")  
	  public void User_login_should_be_successful() { if(driver.getTitle().equalsIgnoreCase("Web Orders")){  
	      System.out.println("Test Pass");  
	   } else {  
	      System.out.println("Test Failed");  
	   }  
	 
	   driver.close();  
	   
	}



	




	}


