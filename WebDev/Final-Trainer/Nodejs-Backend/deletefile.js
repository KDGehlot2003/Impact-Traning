var fs = require('fs');

const filePath = 'test.txt'; // Replace this with your file's path

fs.unlink(filePath, (err) => {
  if (err) {
    console.error('Error removing file:', err);
  } else {
    console.log('File removed successfully');
  }
});