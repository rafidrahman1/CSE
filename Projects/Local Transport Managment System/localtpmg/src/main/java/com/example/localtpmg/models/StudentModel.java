package com.example.localtpmg.models;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class StudentModel {
    private Long id;
    private String name;
    private Double cgpa;
    private Double creditCompleted;
}
