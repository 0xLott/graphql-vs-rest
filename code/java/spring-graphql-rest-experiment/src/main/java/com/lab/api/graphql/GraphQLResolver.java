package com.lab.api.graphql;

import com.lab.api.repository.CommentRepository;
import com.netflix.graphql.dgs.DgsComponent;
import com.netflix.graphql.dgs.DgsDataFetchingEnvironment;
import com.netflix.graphql.dgs.DgsQuery;
import com.netflix.graphql.dgs.InputArgument;
import lombok.RequiredArgsConstructor;

@DgsComponent
@RequiredArgsConstructor
public class GraphQLResolver {

    private final CommentRepository commentRepository;

    @DgsQuery
    public Object commentById(@InputArgument Long id, DgsDataFetchingEnvironment dfe) throws Exception {
        return commentRepository.findById(id).orElseThrow();
    }

    @DgsQuery
    public Object commentsByUserId(@InputArgument Long id, DgsDataFetchingEnvironment dfe) throws Exception {
        return commentRepository.findByUserId(id);
    }

    @DgsQuery
    public Object commentsByMinScore(@InputArgument Integer score, DgsDataFetchingEnvironment dfe) throws Exception {
        return commentRepository.findByScoreGreaterThanEqual(score);
    }

    @DgsQuery
    public Object allComments(DgsDataFetchingEnvironment dfe) throws Exception {
        return commentRepository.findAll();
    }
}
