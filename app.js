const express=require('express');
const axiox=require('axios');
const mysql=require('mysql');
const cors = require('cors');
const jwt=require("jsonwebtoken");
const nodemailer=require("nodemailer");
const cookieParser=require("cookie-parser");
const bodyParser=require('body-parser');
//create connection
const app=express();
app.use(cors({
credentials:true,
origin:['http://localhost:5173']
}));
app.use(bodyParser.json());
app.use(cookieParser());
const db=mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'',
    database:'loginusers',
});
app.use((req,res,next)=>{
res.header("Access-Control-Allow-Origin","*");
res.header(
  "Access-Control-Allow-Headers",
  "Origin, X-Requested-With, Content-Type, Accept, Authorization"
);
if(req.method=="OPTIONS"){
res.header("Access-Control-Allow-Methods",'PUT, POST, DELETE, GET, PATCH');
return res.status(200).json({});
}
next();
});
db.connect((err)=>{
  if(err){
    console.log("error connecting");return;
  }
  else{
console.log("connected");}
})
app.post("/getusers",(req,res)=>{
  const {email}=req.body;
let sql=db.query('SELECT * FROM users WHERE email = ? ',[email],(err,result)=>{
  res.json(result);
  console.log(result);
});
// let query=db.query(sql,(err,result)=>{
// res.json(result);
// });
});
app.post("/login",(req,res)=>{
  const {email, password}=req.body;
 // const username=db.query('SELECT username FROM users WHERE email = ? ',[email]);
  var isloggedin;
  let query1=db.query('SELECT * FROM users WHERE email = ? ',[email],(err,result)=>{
    
    if (err) {
      console.error('Error executing SQL query:', err);
      return res.status(500).send('Internal server error');
    }
     // Check if any records were returned
     if (result.length === 0) {
      return res.status(401).send('Invalid email or password');
    }
      if(result[0].email===email && result[0].password===password)
        {
          const token=jwt.sign({_email:email,_password:password,_username:result[0].username,_phonenumber:result[0].phonenumber,_country:result[0].country,_headline:result[0].headline},"secret");
          res.cookie('jwt',token,{
            httpOnly:true,
          }).status(200).send(token);  
      }else{
          res.status(401).send('Invalid email or password');
        }
       
  });
  app.post("/send",(req,res)=>{
    const email=req.body;
    var code=Math.floor(Math.random()*100000);
var transporter=nodemailer.createTransport({
  service:'gmail',
  auth:{
    user:"leenhija171@gmail.com",
    pass:"Leen.0796315448"
  }
});
var mailOptions={
  from:"leenhija171@gmail.com",
  to:email,
  subject:"verification code",
  text:`${code} is your verification code please use it to verify your account`
};
transporter.sendMail(mailOptions,(error,info)=>{
  if(error){
  console.log(error)}
  else{
    res.status(201).json({ message: 'verification code sent successfully'});  }
})
  })
app.post("/signup",(req,res)=>{
const {username,phonenumber,email,password}=req.body;
const newUser={username,phonenumber,email,password};
console.log(newUser);
db.query('INSERT INTO users SET ?',newUser,(err,result)=>{
  if(err){
    console.log(err);
    res.status(500).json({ error: 'Failed to create user' });
      return;
  }
  res.status(201).json({ message: 'User created successfully'});
})
});

});
app.get("/user",async(req,res)=>{
    const token = req.headers.authorization.split(' ')[1]; 
    jwt.verify(token, 'secret', (err, decoded) => {
      if (err) {
        console.error('JWT verification error:', err);
        return res.status(401).send('Unauthorized');
      }
  
      const userEmail = decoded._email; 
      const userName=decoded._username;
      const phone_number=decoded._phonenumber;
      const user_country=decoded._country;
      const HeadLine=decoded._headline;
      res.status(200).json({ email: userEmail ,username:userName,phonenumber:phone_number,country:user_country,headline:HeadLine});
    });
  });
app.put('/add_country_and_headline',async(req,res)=>{
const {country,headline,email}=req.body;
try{
  if(country!='' && headline!=''){
db.query(`UPDATE users SET country = ? , headline = ? WHERE email = ?`,[country,headline,email],(err,result)=>{
if(err){
  console.log(err);
    res.status(500).json({ error: 'Failed to add country' });
      return;
}else{
  return res.status(200).json({ message: 'Profile updated successfully'});
}
})}else if (country!='' && headline==''){
  db.query(`UPDATE users SET country = ? WHERE email = ?`,[country,email],(err,result)=>{
    if(err){
      console.log(err);
        res.status(500).json({ error: 'Failed to add country' });
          return;
    }else{
      return res.status(200).json({ message: 'Profile updated successfully'});
    }
    })
}else if (country=='' && headline!=''){
  db.query(`UPDATE users SET headline = ? WHERE email = ?`,[headline,email],(err,result)=>{
    if(err){
      console.log(err);
        res.status(500).json({ error: 'Failed to add country' });
          return;
    }else{
      return res.status(200).json({ message: 'Profile updated successfully'});
    }
    })
}
} catch (error) {
console.error('Error updating profile:', error);
return res.status(500).json({ message: 'Internal server error' });
}
})
   app.put('/change_password',async(req,res)=>{
    const {oldpassword,newpassword,email}=req.body;
    try{
      if(oldpassword!=newpassword){
     db.query('UPDATE users SET password = ? WHERE email = ?',[newpassword,email],(err,result)=>{
      return res.status(200).json({ message: 'Profile updated successfully'});
     })}
     else{
      return res.status(403).json({message:'this password already exists'});
     }
    }catch{
      console.error('Error updating profile:', error);
      return res.status(500).json({ message: 'Internal server error' });
    }
   })  
app.listen("5000",()=>{
console.log("server is connected");
})