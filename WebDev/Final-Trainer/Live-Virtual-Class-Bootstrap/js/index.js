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



function result() {
    var q1 = document.getElementsByName('q1')
    var q2 = document.getElementsByName('q2')
    let marks = 0
    if(document.querySelector('input[name="q1"]:checked').value=="true"){
        marks+=1
    } 
    if(document.querySelector('input[name="q2"]:checked').value=="true"){
        marks+=1
    } 
    alert("You got " + marks + " Marks 🥳")
    console.log(marks)
}


function fun5() {

    // window.open("window.html","","width:800 height=800")
}