import React from 'react';
import './style.css';

const Feed = ({links, similarity, title, sentence, total_words}) => {

    return (
        <div class='feed'>
            <div class='row'>
                <h2 class='feed-title'><a href={links}target="_blank" rel="noreferrer">{title}</a></h2>
                <div class='feed-text'><p>{sentence}</p></div>
            </div>
            <div class='row'>
                <div class='col-3'>
                    <div class='row feed-subtext-title'>Total Words</div>
                    <div class='row feed-subtext-info'>{total_words}</div>
                </div>
                <div class='col-3'>
                    <div class='row feed-subtext-title'>Similarity</div>
                    <div class='row feed-subtext-info' >{Math.round((similarity + Number.EPSILON) * 100)}%</div>
                </div>
                <div class='col'></div>
            </div>

        </div>
    );
};

export default Feed;
