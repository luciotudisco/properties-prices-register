import { Box, Typography } from "@mui/material";
import FavoriteTwoToneIcon from "@mui/icons-material/FavoriteTwoTone";

const Footer = function (): JSX.Element {
  return (
    <Box className="flex w-full h-full justify-center align-middle items-center bg-black border-t-2 border-gray-700">
      <Typography
        className="text-white"
        variant="caption"
        fontFamily="monospace"
      >
        Made with{" "}
        <FavoriteTwoToneIcon style={{ fill: "red" }} fontSize="small" /> in
        Ballymore Eustace
      </Typography>
    </Box>
  );
};

export default Footer;
