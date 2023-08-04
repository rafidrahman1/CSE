package com.example.localtpmg.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/student")
public class StudentController {

    @GetMapping("/all")
    public ResponseEntity<StudentEntity> getAllStudent(){

        //all student return hobe
        return null;
    }

    @GetMapping //http request to get info from database
    public ResponseEntity<StudentEntity> getStudentByID(long studentID){

        //1 ta student
        return null;
    }

    @PostMapping //http request to post in database
    public ResponseEntity<StudentEntity> createStudent(StudentModel studentModel){

        return null;
    }
}
