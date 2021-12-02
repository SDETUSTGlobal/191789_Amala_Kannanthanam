package login;
 import org.openqa.selenium.By;   
import org.openqa.selenium.WebDriver;   
import org.openqa.selenium.WebElement;   
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;  
import cucumber.annotation.en.Given;   
import cucumber.annotation.en.Then;   
import cucumber.annotation.en.When;   


public class Step {
	WebDriver  driver = null;
			  @Given("^I am on user login page$")   
			   public void goToSmart() {  
				 System.setProperty("webdriver.chrome.driver", "D://eclipse1//Sel_jar//chromedriver_win32//chromedriver.exe");
				 driver= new ChromeDriver();
				 driver.navigate().to("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx");
			    
			   }   
			  @When("^I enter valid data on the page$")   
			   public void enterData(){
				    driver.findElement(By.id("ctl00_MainContent_username")).sendKeys("Tester");
				   	driver.findElement(By.id("ctl00_MainContent_password")).sendKeys("test");
				   	driver.findElement(By.id("ctl00_MainContent_login_button")).click();
			   }
			  @Then("^User registration should be successful$")   
			   public void User_registration_should_be_successful() {  
			      if(driver.getTitle().equalsIgnoreCase("Web Orders"))
			      {  
			         System.out.println("Test Pass");   
			      } else 
			      {   
			         System.out.println("Test Failed");   
			      }   
			      driver.close();   
			   }}