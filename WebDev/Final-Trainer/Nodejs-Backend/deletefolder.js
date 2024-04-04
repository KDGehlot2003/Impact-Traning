const fs = require('fs'); 



fs.rmdir("test", () => { 
console.log("Folder Deleted!"); 

// Get the current filenames 
// in the directory to verify 
// getCurrentFilenames(); 
}); 


// Function to get current filenames 
// in directory 


// function getCurrentFilenames() { 
// console.log("\nCurrent filenames:"); 
// fs.readdirSync(__dirname).forEach(file => { 
// 	console.log(file); 
// }); 
// console.log("\n"); 
// } 
