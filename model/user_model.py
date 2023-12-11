from flask import Flask, render_template, session, redirect, url_for,jsonify
import mysql.connector
import json


class user_model():
    def __init__(self):
            try:
               self.con=mysql.connector.connect(host="localhost",user="root",password="nineleaps",database="IPL")
               self.con.autocommit=True
               self.cur=self.con.cursor(dictionary=True)
               print("Connection Successful")
            except:
                print("Some error")

    def user_getall_model(self):
      self.cur.execute("select * from IPLfinal where SOLD=0")
      result=self.cur.fetchall()
      if len(result)>0:
             return json.dumps(result)
      else:
            return "NO DATA FOUND"

    def user_addone_model(self,data):
      self.cur.execute("INSERT INTO KKR(Id, Name, Price) VALUES (%s, %s, %s)",
                         (data['id'], data['name'], data['price']))
      return "Player added successfully"

    def user_update_model(self,data):
      player_id = data.get('id')
      print(f"Updating player with ID: {player_id}")
      self.cur.execute(f"UPDATE IPLfinal SET Sold = 1 WHERE PlayerID=%s", (player_id,))
      if self.cur.rowcount>0:
        return "User Updated Successfully"
      else:
          return "Nothing to update"
          
      
      
    def get_next_batsman(self):
        try:
            if 'batsman_index' not in session:
                session['batsman_index'] = 1

            self.cur.execute("SELECT * FROM IPLfinal WHERE TYPE='batsman' AND SOLD=0 LIMIT 1 OFFSET %s", (session['batsman_index'] - 1,))
            batsman = self.cur.fetchone()

            if batsman:
                session['batsman_index'] += 1
                return json.dumps(batsman)
            else:
                # Reset the index when all batsmen are displayed
                session['batsman_index'] = 1
                return "NO DATA FOUND"
        except Exception as e:
            print(f"Error: {e}")
            return "Internal Server Error"

    
    def get_next_bowler(self):
        try:
            if 'bowler_index' not in session:
                session['bowler_index'] = 1

            self.cur.execute("SELECT * FROM IPLfinal WHERE (TYPE='fast bowler' OR TYPE='spin bowler') AND SOLD=0 LIMIT 1 OFFSET %s", (session['bowler_index'] - 1,))
            bowler = self.cur.fetchone()

            if bowler:
                session['bowler_index'] += 1
                return json.dumps(bowler)
            else:
                # Reset the index when all batsmen are displayed
                session['bowler_index'] = 1
                return "NO DATA FOUND"
        except Exception as e:
            print(f"Error: {e}")
            return "Internal Server Error"


    def get_next_allrounder(self):
        try:
            if 'allrounder_index' not in session:
                session['allrounder_index'] = 1

            self.cur.execute("SELECT * FROM IPLfinal WHERE TYPE='All Rounder' AND SOLD=0 LIMIT 1 OFFSET %s", (session['bowler_index'] - 1,))
            allrounder = self.cur.fetchone()

            if allrounder:
                session['allrounder_index'] += 1
                return json.dumps(allrounder)
            else:
                # Reset the index when all batsmen are displayed
                session['allrounder_index'] = 1
                return "NO DATA FOUND"
        except Exception as e:
            print(f"Error: {e}")
            return "Internal Server Error"