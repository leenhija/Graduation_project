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
  let query1=db.query('SELECT email,password,username FROM users WHERE email = ? ',[email],(err,result)=>{
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
          const token=jwt.sign({_email:email,_password:password,},"secret");
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
      const userName=decoded._username
      res.status(200).json({ email: userEmail ,username:userName});
    });
  });

     
app.listen("5000",()=>{
console.log("server is connected");
})