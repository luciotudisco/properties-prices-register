import { NextApiRequest, NextApiResponse } from "next";

/**
 * Handles the health check API request.
 *
 * @param request - The NextApiRequest object.
 * @param response - The NextApiResponse object.
 */
export default function handler(
  request: NextApiRequest,
  response: NextApiResponse,
) {
  response.status(200).json({ status: "ok" });
}
