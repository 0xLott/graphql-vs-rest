package com.lab.api.entity;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.*;

import java.util.Date;

@Entity
@Table(name = "comments")
public class Comment {
    @Id
    @JsonProperty("_Id")
    private Long id;

    @Column(name = "post_id")
    @JsonProperty("_PostId")
    private Long postId;

    @JsonProperty("_Score")
    private Integer score;

    @JsonProperty("_Text")
    private String text;

    @JsonProperty("_CreationDate")
    @Column(name = "creation_date")
    private Date creationDate;

    @JsonProperty("_UserId")
    @Column(name = "user_id")
    private Long userId;

    public void setText(String text) {
        this.text = (text != null && text.length() > 255) ? text.substring(0, 255) : text;
    }
}
