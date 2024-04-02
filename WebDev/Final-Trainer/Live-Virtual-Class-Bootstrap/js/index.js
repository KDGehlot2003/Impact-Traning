function cal_sal(){
    var sal=eval(form1.num1.value);
    var per=form1.perfor.value;

    if (per=='a'){
        var bonu=sal*0.3;
        form1.bonus.value=bonu;
        form1.salary.value=sal+bonu

    }
    else if(per=='b'){
        var bonu=sal*0.1;
        form1.bonus.value=bonu;
        form1.salary.value=sal+bonu
    }
    else{
        form1.bonus.value='No Bonus'
        form1.salary.value=sal
    }
}