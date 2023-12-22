import { Navigate } from 'react-router-dom'
import { toast } from "react-toastify";
import { PostButton } from '../components/postbutton';
import { useBackendMutation } from '../utils/useBackend';
import BasicLayout from '../layouts/BasicLayout';
import { useState } from 'react';

export default function PostButtonPage({storybook=false}) {
    
    const [id, setId] = useState(0);


    const objectToAxiosParams = () => ({
        url: "/api/restaurants/post",
        method: "POST",
        params: {
        ID: id,
        Time: Date.now(),
        }
    });

    const onSuccess = () => {
        toast(`New db entry Created - id: ${id}`);
        setId(id + 1);
    }

    const mutation = useBackendMutation(
        objectToAxiosParams,
        { onSuccess }, 
        // Stryker disable next-line all : hard to set up test for caching
        ["/api/post_time"] // mutation makes this key stale so that pages relying on it reload
        );

    const { isSuccess } = mutation

    const onSubmit = async (data) => {
        mutation.mutate(data);
    }

    if (isSuccess && !storybook) {
        return <Navigate to="/" />
    }

    return (
        <BasicLayout>
        <div>
            <PostButton onButtonClick={onSubmit} />
        </div>
        </BasicLayout>
    )
}