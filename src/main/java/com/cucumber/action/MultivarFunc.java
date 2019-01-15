package com.cucumber.action;

public class MultivarFunc {

    private float num1;
    private float num2;
    private boolean result;

    public void setNum1(float num1) {
        this.num1 = num1;
    }

    public void setNum2(float num2) {
        this.num2 = num2;
    }

    public boolean getResult() {
        return result;
    }

    public void calculate() {
        result = (4<this.num1 && this.num1<6 && 3<this.num2 && this.num2<7);
    }
}