package com.cucumber;
import com.cucumber.action.MultivarFunc;
import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import static org.junit.Assert.*;

public class MyStepdefs {


    private MultivarFunc multivarFunc;


    @Given("^i input \"([^\"]*)\" and \"([^\"]*)\"$")
    public void iInputAnd(String arg0, String arg1) {

        multivarFunc = new MultivarFunc();
        multivarFunc.setNum1(Float.parseFloat(arg0));
        multivarFunc.setNum2(Float.parseFloat(arg1));

    }

    @When("^the function is run$")
    public void theFunctionIsRun() {

        multivarFunc.calculate();
    }

    @Then("^the output should be \"([^\"]*)\"$")
    public void theOutPutShouldBe(String arg0) {

        assertEquals(Boolean.parseBoolean(arg0), multivarFunc.getResult());
    }

}
