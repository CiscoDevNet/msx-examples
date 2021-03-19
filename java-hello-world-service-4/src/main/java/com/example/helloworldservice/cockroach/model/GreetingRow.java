//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.cockroach.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder(toBuilder = true)
@Entity
@Table
public class GreetingRow {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private UUID greetingId;

    @ManyToOne(targetEntity = com.example.helloworldservice.cockroach.model.LanguageRow.class)
    @JoinColumn(name = "language_id")
    private com.example.helloworldservice.cockroach.model.LanguageRow language;

    @Column(length = 128)
    private String value;
}