'use strict';

var app = require('electron').app;
var BrowserWindow = require('electron').BrowserWindow;
var fs = require('fs');

var mainWindow = null;

app.on('ready', function() {
	mainWindow = new BrowserWindow({
		height: 600,
		width: 800,
		title: "LVC native"
	});

	mainWindow.on('closed', () => {
		mainWindow = null
	});

	mainWindow.loadURL('file://' + __dirname + '/app/View/index.html');

	var contents = mainWindow.webContents

	fs.readFile(__dirname + '/app/css/styles.css', 'utf8', function(err, css){
		contents.insertCSS(css);
	});
	
	fs.readFile(__dirname + '/app/ConnectionManager.min.js', 'utf8', function(err, js){
		contents.executeJavaScript(js);
	});

	fs.readFile(__dirname + '/app/Controller/indexViewController.min.js', 'utf8', function(err, js){
		contents.executeJavaScript(js);
	});
})