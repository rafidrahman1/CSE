package com.example.localtpmg.controller;

import com.example.localtpmg.entity.StudentEntity;
import com.example.localtpmg.models.StudentModel;
import com.example.localtpmg.service.StudentService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/student")
@RequiredArgsConstructor

public class StudentController {

    private final StudentService studentService;
    @GetMapping("/all")
    public ResponseEntity<List<StudentEntity>> getAllStudent(){
        List<StudentEntity> allStudent = studentService.getStudentList();

        //all student return hobe
        return new ResponseEntity<>(allStudent, HttpStatus.OK);
    }

    @GetMapping //http request to get info from database
    public ResponseEntity<StudentEntity> getStudentByID(long studentID){

        //1 ta student
        return null;
    }

    @PostMapping("/create") //http request to post in database
    public ResponseEntity<StudentEntity> createStudent(@RequestBody StudentModel studentModel){

        StudentEntity studentEntity = studentService.createStudent(studentModel);

        return new ResponseEntity<>(studentEntity, HttpStatus.OK);
    }
}
