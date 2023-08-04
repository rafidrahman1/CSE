package com.example.localtpmg.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name= "student-entity")
@Data //getter setter
@AllArgsConstructor //no need write constructors
@NoArgsConstructor //default constructors
@Builder
public class StudentEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private Double cgpa;
    private Double creditCompleted;
}
