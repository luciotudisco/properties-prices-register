import { Box, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import Lottie from "react-lottie-player";

const EmptyHits = function (): JSX.Element {
  const [animationData, setAnimationData] = useState<object>();

  useEffect(() => {
    import("./assets/no-results-lottie.json").then(setAnimationData);
  }, []);

  if (!animationData) return <div>Loading...</div>;
  return (
    <Box className="flex flex-col w-full h-full align-middle items-center gap-5">
      <Lottie animationData={animationData} loop play />
      <Typography className="text-gray-500" variant="body2" fontSize="small">
        No results found
      </Typography>
    </Box>
  );
};

export default EmptyHits;
